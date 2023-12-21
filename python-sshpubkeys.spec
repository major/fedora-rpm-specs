Name:           python-sshpubkeys
Version:        3.3.1
Release:        %autorelease
Summary:        OpenSSH public key parser for Python

License:        BSD-3-Clause
URL:            https://github.com/ojarva/sshpubkeys
Source:         %{url}/archive/%{version}/sshpubkeys-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
Native implementation for validating OpenSSH public keys.

Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves
are supported.}


%description %{common_description}


%package -n     python3-sshpubkeys
Summary:        %{summary}

%description -n python3-sshpubkeys %{common_description}


%prep
%autosetup -n python-sshpubkeys-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l sshpubkeys


%check
%{py3_test_envvars} %{python3} -m unittest tests


%files -n python3-sshpubkeys -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
