Summary:	Utilities belonging to the Reiser4 filesystem
Summary(pl):	Narzêdzia dla systemu plików Reiser4
Summary(pt_BR):	Este pacote contém os utilitários para manipulação do sistema de arquivos Reiser4
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ÒÏÂÏÔÙ Ú ÆÁÊÌÏ×ÏÀ ÓÉÓÔÅÍÏÀ Reiser4
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ ÒÁÂÏÔÙ Ó ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÏÊ Reiser4
Name:		reiser4progs
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.namesys.com/pub/reiser4progs/%{name}-%{version}.tar.gz
# Source0-md5:	da64ff2266d854ffab67faf18eb8f370
Patch0:		%{name}-am18.patch
Patch1:		%{name}-opt.patch
URL:		http://www.reiserfs.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libaal-devel >= 1.0.2
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libuuid-devel
BuildRequires:	readline-devel
Requires:	libaal >= 1.0.2
Obsoletes:	reiserfs-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
naprawiania b³êdów (reiser4fsck) oraz zmiany wielko¶ci
(resize_reiser4) systemu plików Reiser4.

%description -l pt_BR
Este pacote contém os utilitários para manipulação do sistema de
arquivos Reiser4.

%description -l ru
îÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÒÁÂÏÔÙ Ó ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÏÊ Reiser4.

%description -l uk
îÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÒÏÂÏÔÉ Ú ÆÁÊÌÏ×ÏÀ ÓÉÓÔÅÍÏÀ Reiser4.

%package devel
Summary:	Header files for reiser4progs libraries
Summary(pl):	Pliki nag³ówkowe bibliotek reiser4progs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libaal-devel >= 0.5.0

%description devel
Header files for reiser4progs libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek reiser4progs.

%package static
Summary:	reiser4progs static libraries
Summary(pl):	Statyczne biblioteki reiser4progs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
reiser4progs static libraries.

%description static -l pl
Statyczne biblioteki reiser4progs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
