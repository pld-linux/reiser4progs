%define		snapshot	2003.05.28
%define         snap    %(echo %{snapshot} | tr -d .)

Summary:	Utilities belonging to the Reiser4 filesystem
Summary(pl):	NarzЙdzia dla systemu plikСw Reiser4
Summary(pt_BR):	Este pacote contИm os utilitАrios para manipulaГЦo do sistema de arquivos Reiser4
Summary(uk):	Утил╕ти для роботы з файловою системою Reiser4
Summary(ru):	Утилиты для работы с файловой системой Reiser4
Name:		reiser4progs
Version:	0.4.7
Release:	%{snap}.1
License:	GPL v2
Group:		Applications/System
# Source0-md5:	8b0c930d5cb42d507ba351b110510ae7
Source0:	http://thebsh.namesys.com/snapshots/%{snapshot}/%{name}-%{snap}.tar.gz
URL:		http://www.reiserfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
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
naprawiania bЁЙdСw (reiser4fsck) oraz zmiany wielko╤ci
(resize_reiser4) systemu plikСw Reiser4.

%description -l pt_BR
Este pacote contИm os utilitАrios para manipulaГЦo do sistema de
arquivos Reiser4.

%description -l ru
Набор утилит для работы с файловой системой Reiser4.

%description -l uk
Наб╕р утил╕т для роботи з файловою системою Reiser4.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING CREDITS ChangeLog INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*
%{_mandir}/man*/*
%{_includedir}/*
