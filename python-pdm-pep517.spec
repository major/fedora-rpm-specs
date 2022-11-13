Name:           python-pdm-pep517
Version:        1.0.5
Release:        1%{?dist}
Summary:        Yet another PEP 517 backend

License:        MIT AND Apache-2.0 AND Public Domain AND BSD-3-Clause AND ISC
URL:            https://pdm.fming.dev
Source0:        %{pypi_source pdm-pep517}

BuildArch:      noarch

BuildRequires:  python3-devel python3-setuptools
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  pytest

%global _description %{expand:
This is the backend for PDM projects, while you can also use it alone. It
reads the metadata of PEP 621 format and coverts it to Core metadata.
}

%description %_description

%package -n python3-pdm-pep517
Summary: %{summary}

%description -n python3-pdm-pep517 %_description

%prep
%autosetup -p1 -n pdm-pep517-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pdm

%check
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

%pytest

%files -n python3-pdm-pep517 -f %{pyproject_files}
%{?el9:%{python3_sitelib}/pdm_pep517-%{version}.dist-info/license_files/LICENSE}

%doc README.md
%license LICENSE

%changelog
* Fri Nov 11 2022 Simon de Vlieger <cmdr@supakeen.com> - 1.0.5-1
- bump to 1.0.5-1

* Fri Nov 11 2022 Simon de Vlieger <cmdr@supakeen.com> - 1.0.4-3
- explicit dependency on python3-setuptools, see BZ#2142037

* Fri Oct 14 2022 Simon de Vlieger <cmdr@supakeen.com> - 1.0.4-2
- epel9 needs an extra file.

* Fri Sep 16 2022 Simon de Vlieger <cmdr@supakeen.com> - 1.0.4-1
- Initial version of the package.
