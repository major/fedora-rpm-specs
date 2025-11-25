%global         srcname  asyncssh
%global         desc     Python 3 library for asynchronous client and\
server-side SSH communication. It uses the Python asyncio module and\
implements many SSH protocol features such as the various channels,\
SFTP, SCP, forwarding, session multiplexing over a connection and more.

Name:           python-%{srcname}
Version:        2.21.1
Release:        %autorelease
Summary:        Asynchronous SSH for Python

# Automatically converted from old format: EPL-2.0 or GPLv2+ - review is highly recommended.
License:        EPL-2.0 OR GPL-2.0-or-later
URL:            https://github.com/ronf/asyncssh
Source0:        %pypi_source


BuildArch:      noarch

# required by unittests
BuildRequires:  nmap-ncat
BuildRequires:  openssh-clients
BuildRequires:  openssl
BuildRequires:  python3-gssapi


# for ed25519 etc.
Recommends:     python3-libnacl

# for OpenSSH private key encryption
Suggests:       python3-bcrypt
# for GSSAPI key exchange/authentication
Suggests:       python3-gssapi
# for X.509 certificate authentication
Suggests:       python3-pyOpenSSL
# for U2F etc. support
Suggests:       python3-fido2

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# remove superfluous build dependencies
sed '/pytest-cov/d' tox.ini -i


%generate_buildrequires
%pyproject_buildrequires -t


%build
sed -i '1,1s@^#!.*$@#!%{__python3}@' examples/*.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{__python3} -m unittest discover -s tests -t . -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE COPYRIGHT
%doc README.rst examples


%changelog
%autochangelog
