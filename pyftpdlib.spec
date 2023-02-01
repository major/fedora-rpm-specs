%global desc %{expand: \
Python FTP server library provides a high-level portable interface to easily
write very efficient, scalable and asynchronous FTP servers with Python.
It is the most complete RFC-959 FTP server implementation available for 
Python programming language.}

Name:			pyftpdlib
Version:		1.5.7
Release:		%autorelease
Summary:		Extremely fast and scalable Python FTP server library

License:		MIT
URL:			https://github.com/giampaolo/pyftpdlib
Source0:		%{url}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:		keycert.pem

BuildArch:		noarch

BuildRequires:	help2man
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-psutil
BuildRequires:	python3-pyOpenSSL

%description 
%{desc}

%package -n python3-%{name}
Summary: %{summary}

%description -n python3-%{name} %{desc}
%{desc}

%prep
%autosetup -n %{name}-release-%{version}
cp %{SOURCE1} pyftpdlib/test

# do not copy the test folder
sed -i "s/, 'pyftpdlib.test'//" setup.py
# non-executable-script
sed -i '/env python/d' pyftpdlib/_compat.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
	help2man --no-info --version-string 'ftpbench %{version}' \
		-o %{buildroot}%{_mandir}/man1/ftpbench.1 \
		%{buildroot}%{_bindir}/ftpbench

%check
%pytest -v -k 'not TestCommandLineParser'

%files -n python3-%{name} -f %{pyproject_files}
%doc HISTORY.rst README.rst
%{_bindir}/ftpbench
%{_mandir}/man1/ftpbench.1*

%changelog
%autochangelog
