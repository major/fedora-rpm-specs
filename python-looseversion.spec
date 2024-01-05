%global _description %{expand:
A backwards/forwards-compatible fork of distutils.version.LooseVersion, for
times when PEP-440 isnt what you need.

The goal of this package is to be a drop-in replacement for the original
LooseVersion. It implements an identical interface and comparison logic to
LooseVersion. The only major change is that a looseversion.LooseVersion is
comparable to a distutils.version.LooseVersion, which means tools should not
need to worry whether all dependencies that use LooseVersion have migrated.

If you are simply comparing versions of Python packages, consider moving to
packaging.version.Version, which follows PEP-440. LooseVersion is better suited
to interacting with heterogeneous version schemes that do not follow PEP-440.}

Name:           python-looseversion
Version:        1.3.0
Release:        %{autorelease}
Summary:        Version numbering for anarchists and software realists

License:        PSF-2.0
URL:            https://pypi.org/pypi/looseversion
Source0:        %{pypi_source looseversion}

BuildArch:      noarch

%description %_description

%package -n python3-looseversion
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-looseversion %_description

%prep
%autosetup -n looseversion-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l looseversion

%check
%pytest -v tests.py

%files -n python3-looseversion -f %{pyproject_files}
%doc README.md CHANGES.md

%changelog
%autochangelog
