Summary:	Utilities belonging to the Reiser4 filesystem
Summary(pl.UTF-8):	Narzędzia dla systemu plików Reiser4
Summary(pt_BR.UTF-8):	Este pacote contém os utilitários para manipulação do sistema de arquivos Reiser4
Summary(ru.UTF-8):	Утилиты для работы с файловой системой Reiser4
Summary(uk.UTF-8):	Утиліти для роботы з файловою системою Reiser4
Name:		reiser4progs
Version:	1.0.7
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://kernel.org/pub/linux/utils/fs/reiser4/reiser4progs/%{name}-%{version}.tar.bz2
# Source0-md5:	0f637512ad11f73739e0e44057bd59e2
Patch0:		%{name}-opt.patch
Patch1:		%{name}-libaal.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-libreiser4-no-libmisc.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libaal-devel >= 1.0.5
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libuuid-devel
BuildRequires:	readline-devel
Requires:	libaal >= 1.0.5
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

%description -l pl.UTF-8
Pakiet zawiera programy do tworzenia (mkreiser4), sprawdzania i
naprawiania błędów (reiser4fsck) oraz zmiany wielkości
(resize_reiser4) systemu plików Reiser4.

%description -l pt_BR.UTF-8
Este pacote contém os utilitários para manipulação do sistema de
arquivos Reiser4.

%description -l ru.UTF-8
Набор утилит для работы с файловой системой Reiser4.

%description -l uk.UTF-8
Набір утиліт для роботи з файловою системою Reiser4.

%package devel
Summary:	Header files for reiser4progs libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek reiser4progs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libaal-devel >= 1.0.5

%description devel
Header files for reiser4progs libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek reiser4progs.

%package static
Summary:	reiser4progs static libraries
Summary(pl.UTF-8):	Statyczne biblioteki reiser4progs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libaal-static >= 1.0.5

%description static
reiser4progs static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki reiser4progs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.* $RPM_BUILD_ROOT/%{_lib}
for f in libreiser4 libreiser4-minimal librepair; do
	lib=$(cd $RPM_BUILD_ROOT/%{_lib}; echo $f-1.0.so.*.*.*)
	ln -sf /%{_lib}/$lib $RPM_BUILD_ROOT%{_libdir}/$f.so
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/debugfs.reiser4
%attr(755,root,root) %{_sbindir}/fsck.reiser4
%attr(755,root,root) %{_sbindir}/make_reiser4
%attr(755,root,root) %{_sbindir}/measurefs.reiser4
%attr(755,root,root) %{_sbindir}/mkfs.reiser4
%attr(755,root,root) /%{_lib}/libreiser4-1.0.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libreiser4-1.0.so.7
%attr(755,root,root) /%{_lib}/libreiser4-minimal-1.0.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libreiser4-minimal-1.0.so.7
%attr(755,root,root) /%{_lib}/librepair-1.0.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/librepair-1.0.so.7
%{_mandir}/man8/debugfs.reiser4.8*
%{_mandir}/man8/fsck.reiser4.8*
%{_mandir}/man8/measurefs.reiser4.8*
%{_mandir}/man8/mkfs.reiser4.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreiser4.so
%attr(755,root,root) %{_libdir}/libreiser4-minimal.so
%attr(755,root,root) %{_libdir}/librepair.so
%{_libdir}/libreiser4.la
%{_libdir}/libreiser4-minimal.la
%{_libdir}/librepair.la
%{_includedir}/reiser4
%{_includedir}/repair
%{_aclocaldir}/libreiser4.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libreiser4.a
%{_libdir}/libreiser4-minimal.a
%{_libdir}/librepair.a
