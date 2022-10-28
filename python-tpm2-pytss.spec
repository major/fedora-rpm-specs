%global pypi_name tpm2-pytss
%global _name tpm2_pytss

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        TPM 2.0 TSS Bindings for Python

License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pytss
Source:         %{pypi_source %{pypi_name}}
Patch0:         python-tpm2-pytss-1.2.0-openssl.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
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
# tests are very dependent on the python/openssl versions and fail at various places
# The test test_tools_decode_tpms_nv_public fails on Fedora rawhide now
%pytest --import-mode=append -k "not test_tools_decode_tpms_nv_public" -n %{_smp_build_ncpus}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
* Wed Oct 26 2022 Jakub Jelen <jjelen@redhat.com> - 1.2.0-1
- Official Fedora package (#2135713)

* Tue Apr 12 2022 Traxtopel <traxtopel@gmail.com> - 1.1.0-1
- Initial package.
