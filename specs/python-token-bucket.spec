Name:           python-token-bucket
Version:        0.3.0
Release:        16%{?dist}
Summary:        A Token Bucket implementation

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/falconry/token-bucket
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Temporary, until https://github.com/falconry/token-bucket/pull/24 gets
# merged upstream.
Patch0:         0000-py312-imp.patch
# Drop pytest-runner and "setup.py test" support
# https://github.com/falconry/token-bucket/pull/28
# Cherry-picked on 0.3.0
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch1:         0001-Drop-pytest-runner-and-setup.py-test-support.patch

%global _description %{expand:
The token-bucket package provides an implementation of the token bucket
algorithm suitable for use in web applications for shaping or policing
request rates. This implementation does not require the use of an independent
timer thread to manage the bucket state.
}

%description %_description

%package -n python3-token-bucket
Summary: %{summary}

%description -n python3-token-bucket %_description

%prep
%autosetup -p1 -n token-bucket-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files token_bucket

%check
%tox

%files -n python3-token-bucket -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.3.0-16
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.3.0-14
- Rebuilt for Python 3.14

* Tue Mar 04 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.3.0-13
- Remove BuildRequires on pytest-runner

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Simon de Vlieger <cmdr@supakeen.com> - 0.3.0-5
- Apply patch for Python 3.12 compatibility.

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 supakeen <cmdr@supakeen.com> - 0.3.0-1
- Initial version of the package.
