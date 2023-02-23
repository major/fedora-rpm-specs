Name:           python-trove-classifiers
Version:        2023.2.20
Release:        1%{?dist}
Summary:        Canonical source for classifiers on PyPI (pypi.org)

License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove-classifiers}

# Drop dependency on calver which is not packaged in Fedora.
# This patch is rebased version of upstream PR:
# https://github.com/pypa/trove-classifiers/pull/126/commits/809156bb35852bcaa1c753e0165f1814f2bcedf6
Patch:          Move-to-PEP-621-declarative-metadata.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Canonical source for classifiers on PyPI.
Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.
}

%description %_description

%package -n python3-trove-classifiers
Summary:        %{summary}

%description -n python3-trove-classifiers %_description


%prep
%autosetup -p1 -n trove-classifiers-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files trove_classifiers


%check
%pytest


%files -n python3-trove-classifiers -f %{pyproject_files}
%doc README.*


%changelog
* Tue Feb 21 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 2023.2.20-1
Initial package

