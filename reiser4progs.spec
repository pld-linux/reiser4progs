%define		snapshot	2003.08.11
%define		_snap    %(echo %{snapshot} | tr -d .)

Summary:	Utilities belonging to the Reiser4 filesystem
Summary(pl):	NarzÍdzia dla systemu plikÛw Reiser4
Summary(pt_BR):	Este pacote contÈm os utilit·rios para manipulaÁ„o do sistema de arquivos Reiser4
Summary(uk):	ı‘…Ã¶‘… ƒÃ— “œ¬œ‘Ÿ ⁄ ∆¡ Ãœ◊œ¿ ”…”‘≈Õœ¿ Reiser4
Summary(ru):	ı‘…Ã…‘Ÿ ƒÃ— “¡¬œ‘Ÿ ” ∆¡ Ãœ◊œ  ”…”‘≈Õœ  Reiser4
Name:		reiser4progs
Version:	0.4.11
Release:	0.%{_snap}
License:	GPL v2
Group:		Applications/System
Source0:	http://thebsh.namesys.com/snapshots/%{snapshot}/%{name}-%{version}.tar.gz
# Source0-md5:	f10006b2c0156d9f7e4aff9e2ab74807
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-opt.patch
URL:		http://www.reiserfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	libaal-devel >= 0.4.9
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	reiserfs-utils

%define		_sbindir	/sbin

%description
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms. The results when
compared to the ext2fs conventional block allocation based file system
running under the same operating system and employing the same
buffering code suggest that these algorithms are overall more
efficient, and are becoming more so every passing month. Loosely
speaking, every month we find another performance cranny that needs
work, and we fix it, and every month we find some way of improving our
overall general usage performance. The improvement in small file space
and time performance suggests that we may now revisit a common OS
design assumption that one should aggregate small objects using layers
above the file system layer. Being more effective at small files DOES
NOT make us less effective for other files, this is a general purpose
FS, and our overall traditional FS usage performance is high enough to
establish that. Reiserfs has a commitment to opening up the FS design
to contributions, and we are now now adding plug-ins so that you can
create your own types of directories and files.

%description -l pl
Pakiet zawiera programy do tworzenia (mkreiser4), sprawdzania i
naprawiania b≥ÍdÛw (reiser4fsck) oraz zmiany wielko∂ci
(resize_reiser4) systemu plikÛw Reiser4.

%description -l pt_BR
Este pacote contÈm os utilit·rios para manipulaÁ„o do sistema de
arquivos Reiser4.

%description -l ru
Ó¡¬œ“ ’‘…Ã…‘ ƒÃ— “¡¬œ‘Ÿ ” ∆¡ Ãœ◊œ  ”…”‘≈Õœ  Reiser4.

%description -l uk
Ó¡¬¶“ ’‘…Ã¶‘ ƒÃ— “œ¬œ‘… ⁄ ∆¡ Ãœ◊œ¿ ”…”‘≈Õœ¿ Reiser4.

%package devel
Summary:	Header files for reiser4progs libraries
Summary(pl):	Pliki nag≥Ûwkowe bibliotek reiser4progs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for reiser4progs libraries.

%description devel -l pl
Pliki nag≥Ûwkowe bibliotek reiser4progs.

%package static
Summary:	reiser4progs static libraries
Summary(pl):	Statyczne biblioteki reiser4progs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
reiser4progs static libraries.

%description static -l pl
Statyczne biblioteki reiser4progs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?debug:--disable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/reiser4
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
