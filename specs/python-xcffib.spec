%global srcname xcffib

Summary:   A drop in replacement for xpyb, an XCB python binding
Name:      python-xcffib
Version:   1.9.0
Release:   %autorelease
Source0:   %{pypi_source}
License:   Apache-2.0
URL:       https://github.com/tych0/xcffib
BuildArch: noarch

BuildRequires:  libxcb-devel
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  xeyes
BuildRequires:  xorg-x11-server-Xvfb


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
%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
