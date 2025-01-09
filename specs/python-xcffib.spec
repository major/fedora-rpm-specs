%global srcname xcffib

Summary:   A drop in replacement for xpyb, an XCB python binding
Name:      python-xcffib
Version:   1.6.2
Release:   %autorelease
Source0:   %{pypi_source}
License:   Apache-2.0
URL:       https://github.com/tych0/xcffib
BuildArch: noarch

BuildRequires:  libxcb-devel

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.1.2
BuildRequires:  python%{python3_pkgversion}-six


%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%package -n python%{python3_pkgversion}-xcffib
Summary: A drop in replacement for xpyb, an XCB python binding
Requires:  python%{python3_pkgversion}-cffi
Requires:  libxcb

%description -n python%{python3_pkgversion}-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%prep
%setup -q -n xcffib-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info


%changelog
%autochangelog
