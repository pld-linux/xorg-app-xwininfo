Summary:	xwininfo application - window information utility for X
Summary(pl.UTF-8):	Aplikacja xwininfo - narzędzie informujące o okienkach pod X
Name:		xorg-app-xwininfo
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xwininfo-%{version}.tar.bz2
# Source0-md5:	e2a9bf5ab7f2a0866700a3b49dd8c6bf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xwininfo is a utility for displaying information about windows.
Various information is displayed depending on which options are
selected.

%description -l pl.UTF-8
xwininfo to narzędzie do wyświetlania informacji o okienkach.
Wyświetlane są różne informacje w zależności od wybranych opcji.

%prep
%setup -q -n xwininfo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.1x*
