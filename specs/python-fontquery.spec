%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontquery
%global _description %{expand:
%{srcname} is a toolset to query/compare fonts for Fedora.
}

Name:           python-%{srcname}
Version:        1.36
Release:        %autorelease
Summary:        Font Querying tool for Fedora
License:        MIT
URL:            https://github.com/fedora-i18n/fontquery
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-wheel
BuildRequires:	python%{python3_pkgversion}-termcolor

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Python library for Font Querying tool

%description -n python%{python3_pkgversion}-%{srcname} %_description

This package contains Python library for %{srcname}.

%package -n %{srcname}
Summary: %{summary}
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: fontconfig git-core
Obsoletes: %{srcname}-builder < 1.8-2
Recommends: podman

%description -n %{srcname} %_description

This package contains the end-user executables for %{srcname}.

%package -n %{srcname}-builder
Summary: Image build tools for Font Querying tool
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: buildah podman

%description -n %{srcname}-builder %_description

This package contains the image build tools for %{srcname}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n %{srcname}
%license LICENSE
%doc README.md
%{_bindir}/fontquery
%{_bindir}/fontquery-client
%{_bindir}/fontquery-diff
%{_bindir}/fontquery-pkgdiff
%{_bindir}/fq2html

%files -n %{srcname}-builder
%license LICENSE
%doc README.md
%{_bindir}/fontquery-build

%changelog
%autochangelog
