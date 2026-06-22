%global         forgeurl https://github.com/msoulier/tftpy
Name:           python-tftpy
Version:        0.8.7
%global         tag %{version}
%forgemeta
Release:        %autorelease
Summary:        TFTPy is a pure Python implementation of the Trivial FTP protocol
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Tftpy is a TFTP library for the Python programming language. It includes
client and server classes, with sample implementations. Hooks are included
for easy inclusion in a UI for populating progress indicators. It supports
RFCs 1350, 2347, 2348 and the "tsize" option from RFC 2349.}


%description %_description


%package -n python3-tftpy
Summary:        %summary


%description -n python3-tftpy %_description


%package -n python3-tftpy-cli
Summary:        %summary
Requires: python3-tftpy = %{version}-%{release}


%description -n python3-tftpy-cli %_description


%prep
%forgesetup

# Disable verbose debug logging in tests to speed up build
sed -i 's/logging.DEBUG/logging.WARNING/g' tests/test.py

# Generate missing test data file
dd if=/dev/zero of=tests/640KBFILE bs=1k count=640

%py3_shebang_fix \
        bin/tftpy_client.py \
        bin/tftpy_server.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

install -p -Dm755 bin/tftpy_client.py %{buildroot}%{_bindir}/tftpy_client
install -p -Dm755 bin/tftpy_server.py %{buildroot}%{_bindir}/tftpy_server

%pyproject_save_files -l tftpy


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} ./tests/test.py


%files -n python3-tftpy -f %{pyproject_files}
%doc README.md
%doc ChangeLog.md


%files -n python3-tftpy-cli
%{_bindir}/tftpy_client
%{_bindir}/tftpy_server


%changelog
%autochangelog
