%global pypi_name tpm2-pytss
%global _name tpm2_pytss

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        3%{?dist}
Summary:        TPM 2.0 TSS Bindings for Python

License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pytss
Source:         %{pypi_source %{pypi_name}}
# https://github.com/tpm2-software/tpm2-pytss/pull/585
Patch1:         %{name}-2.3.0-secp192.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{undefined rhel}
BuildRequires:  python3-pytest-xdist
%endif
BuildRequires:  tpm2-tss-devel >= 2.0.0
BuildRequires:  gcc
# for tests
BuildRequires:  swtpm
BuildRequires:  tpm2-tools

%global _description %{expand:
TPM2 TSS Python bindings for Enhanced System API (ESYS), Feature API (FAPI),
Marshaling (MU), TCTI Loader (TCTILdr) and RC Decoding (rcdecode) libraries.
It also contains utility methods for wrapping keys to TPM 2.0 data structures
for importation into the TPM, unwrapping keys and exporting them from the TPM,
TPM-less makecredential command and name calculations, TSS2 PEM Key format
support, importing Keys from PEM, DER and SSH formats, conversion from
tpm2-tools based command line strings and loading tpm2-tools context files.
}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{_name}


%check
%pyproject_check_import
%ifarch s390x
# this test does not work for some reason on the s390x as it times out
%global testargs -k "not test_spi_helper_good"
%endif
%pytest --import-mode=append %{?!rhel:-n 1} %{?testargs}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Jakub Jelen <jjelen@redhat.com> - 2.3.0-1
- New upstream release (#2295581)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.13

* Mon May 27 2024 Jakub Jelen <jjelen@redhat.com> - 2.2.1-2
- Fix build issue in rawhide (#2283520)

* Tue Mar 05 2024 Jakub Jelen <jjelen@redhat.com> - 2.2.1-1
- New upstream release (#2149103)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Jakub Jelen <jjelen@redhat.com> - 2.1.0-3
- Enable tests on i686 again

* Wed Aug 16 2023 Jakub Jelen <jjelen@redhat.com> - 2.1.0-2
- Enable builds on i686 again
- Fix another test issues

* Mon Aug 07 2023 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#2149103)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Jakub Jelen <jjelen@redhat.com> - 1.2.0-1
- Official Fedora package (#2135713)

* Tue Apr 12 2022 Traxtopel <traxtopel@gmail.com> - 1.1.0-1
- Initial package.
