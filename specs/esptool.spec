Name:           esptool
Version:        4.8.1
Release:        %autorelease
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32

License:        GPL-2.0-or-later
URL:            https://github.com/espressif/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/espressif/esptool/issues/1013
Patch:          Don-t-test-ecdsa192-it-s-unsupported-on-Fedora.patch
# https://github.com/espressif/esptool/pull/1055
Patch:          https://github.com/espressif/esptool/pull/1055.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pyelftools
BuildRequires:  python3-requests

Provides:       %{name}.py = %{version}-%{release}


%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 & ESP32 WiFi microcontroller. Allows flashing firmware,
reading back firmware, querying chip parameters, etc.
Developed by the community, not by Espressif Systems.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files esptool espefuse espsecure esp_rfc2217_server
for NAME in %{name} espefuse espsecure esp_rfc2217_server ; do
  ln -s ./$NAME.py %{buildroot}%{_bindir}/$NAME
done


%check
# There is esptool[hsm] which pulls additional requirement on python-pkcs11
# It is not yet packaged in Fedora though
%pyproject_check_import -e 'espsecure.esp_hsm_sign*'
%pytest -m host_test --ignore test/test_espsecure_hsm.py


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/espefuse
%{_bindir}/espefuse.py
%{_bindir}/espsecure
%{_bindir}/espsecure.py
%{_bindir}/esp_rfc2217_server
%{_bindir}/esp_rfc2217_server.py


%changelog
%autochangelog
