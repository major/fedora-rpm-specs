%global pypi_name tpm2-pytss
%global _name tpm2_pytss

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        %autorelease
Summary:        TPM 2.0 TSS Bindings for Python

License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pytss
Source:         %{pypi_source %{pypi_name}}
# https://github.com/tpm2-software/tpm2-pytss/pull/585
Patch1:         %{name}-2.3.0-secp192.patch
# https://github.com/tpm2-software/tpm2-pytss/pull/589
Patch2:         %{name}-bsd.patch
# https://github.com/tpm2-software/tpm2-pytss/pull/615
Patch3:         %{name}-gcc15.patch
# cryptograpy: add copy dunder for private keys
# cryptography >= 45.0.0 requires the copy dunder for private key implementations.
# https://github.com/tpm2-software/tpm2-pytss/commit/6ab4c74e6fb3da7cd38e97c1f8e92532312f8439
Patch4:         %{name}-copy-dunder.patch
# cryptography: fix support for cryptography 47.
Patch5:         %{name}-cryptography47.patch
# crypto: fix deprection warnings (backport)
Patch6:         %{name}-cryptography-decrepit.patch
# Drop redundant BuildRequires for python3-wheel
# https://github.com/fedora-eln/eln/issues/284
Patch7:         https://github.com/tpm2-software/tpm2-pytss/commit/3107f615.patch
# cd433019cf109986d523ab4dc644af723f6f0d59
# dba34b3a0af39122381d613a7beb3a0d46b7ae21
# 6e02235e03eaab003d0bb94fd70ea16c684e6ff4
# 9cc11edbe174dc71cf77c841b5a99717a85b7471
Patch8:         python-tpm2-pytss-raw-regex.patch

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
export OPENSSL_ENABLE_SHA1_SIGNATURES=1
%pyproject_check_import
# The test test_tools_decode_tpml_tagged_tpm_property checks TPM2 revision which is not stable
# In upstream this test as well as the tools are removed so I do not have any good way to fix it
%ifarch s390x
# this test does not work for some reason on the s390x as it times out
%global testargs -k "not test_spi_helper_good and not test_tools_decode_tpml_tagged_tpm_property"
%else
%global testargs -k "not test_tools_decode_tpml_tagged_tpm_property"
%endif
%pytest --import-mode=append %{?!rhel:-n 1} %{?testargs}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
