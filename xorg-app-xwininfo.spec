#
# Conditional build:
%bcond_without	xcb_errors	# system xcb-errors library
%bcond_without	xcb_icccm	# system xcb-icccm library

Summary:	xwininfo application - window information utility for X
Summary(pl.UTF-8):	Aplikacja xwininfo - narzędzie informujące o okienkach pod X
Name:		xorg-app-xwininfo
Version:	1.1.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xwininfo-%{version}.tar.xz
# Source0-md5:	c91201bc1eb5e7b38933be8d0f7f16a8
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
# xcb >= 1.6 xcb-shape
BuildRequires:	libxcb-devel >= 1.6
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
%{?with_xcb_errors:BuildRequires:	xcb-util-errors-devel >= 1.0}
%{?with_xcb_icccm:BuildRequires:	xcb-util-wm-devel >= 0.3.8}
BuildRequires:	xz
Requires:	libxcb >= 1.6
%{?with_xcb_errors:Requires:	xcb-util-errors >= 1.0}
%{?with_xcb_icccm:Requires:	xcb-util-wm >= 0.3.8}
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
%configure \
	%{?with_xcb_errors:--with-xcb-errors} \
	%{?with_xcb_icccm:--with-xcb-icccm}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.1*
