Summary:	RENDER extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia RENDER
Name:		xorg-proto-renderproto
Version:	0.11.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{version}.tar.bz2
# Source0-md5:	a914ccc1de66ddeb4b611c6b0686e274
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Rendering (RENDER) extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia RENDER.

%package devel
Summary:	RENDER extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia RENDER
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	render
Obsoletes:	renderext

%description devel
X Rendering (RENDER) extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia RENDER.

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
%doc COPYING ChangeLog README renderproto.txt
%{_includedir}/X11/extensions/render*.h
%{_pkgconfigdir}/renderproto.pc
