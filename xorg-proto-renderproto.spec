# $Rev: 3261 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	Render protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Render i pomocnicze
Name:		xorg-proto-renderproto
Version:	0.9
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/renderproto-%{version}.tar.bz2
# Source0-md5:	358e263c627aa1d44094cbdb1e883a99
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/renderproto-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Render protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Render i pomocnicze.


%package devel
Summary:	Render protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Render i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Render protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Render i pomocnicze.


%prep
%setup -q -n renderproto-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/renderproto.pc
