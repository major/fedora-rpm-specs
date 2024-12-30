%define unmangled_name proton-core
%define github_repo_name python-proton-core

Name: python-%{unmangled_name}
Version: 0.3.3
Release: %{autorelease}
Summary: %{unmangled_name} library

License: GPL-3.0-or-later
URL:     https://github.com/ProtonVPN/%{github_repo_name}
Source:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
# Test requirements
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pyotp)
BuildArch: noarch

%global _description %{expand:
The %{unmangled_name} component contains core logic used by the other ProtonVPN
components, such as API and SSO. }

%description %_description

%package -n python3-%{unmangled_name}
Summary: %{summary}
Conflicts: python3-proton-client

%description -n python3-%{unmangled_name} %_description

%prep
%autosetup -p1 -n %{github_repo_name}-%{version}
# Do not measure test coverage
sed -i '/addopts = --cov=proton --cov-report html --cov-report term/d' setup.cfg 

%generate_buildrequires
%pyproject_buildrequires -r
 
%build
%pyproject_wheel
 
%install
%pyproject_install
 
%pyproject_save_files proton
 
%check
%pyproject_check_import

k="${k-}${k+ and }not (TestAlternativeRouting and test_alternative_routing_works_on_prod)"
k="${k-}${k+ and }not (TestAuto and test_auto_works_on_prod)"
k="${k-}${k+ and }not (TestProtonSSO and test_broken_data)"
k="${k-}${k+ and }not (TestProtonSSO and test_broken_index)"
k="${k-}${k+ and }not (TestProtonSSO and test_sessions)"
k="${k-}${k+ and }not (TestSession and test_ping)"
k="${k-}${k+ and }not (TestTLSValidation and test_successful)"
k="${k-}${k+ and }not (TestTLSValidation and test_without_pinning)"
k="${k-}${k+ and }not (TestTLSValidation and test_bad_pinning_fingerprint_changed)"
k="${k-}${k+ and }not (TestTLSValidation and test_bad_pinning_url_changed)"

%pytest -k "${k-}"

%files -n python3-%{unmangled_name} -f %{pyproject_files}

%changelog
%autochangelog
