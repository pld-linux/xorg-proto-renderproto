Summary:	Render protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Render i pomocnicze
Name:		xorg-proto-renderproto
Version:	0.11
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{version}.tar.bz2
# Source0-md5:	b160a9733fe91b666e74fca284333148
Patch0:		%{name}-undefined_XID.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Render protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Render i pomocnicze.

%package devel
Summary:	Render protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Render i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	render
Obsoletes:	renderext

%description devel
Render protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Render i pomocnicze.

%prep
%setup -q -n renderproto-%{version}
%patch0 -p1

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/renderproto.pc
