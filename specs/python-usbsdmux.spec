%global srcname usbsdmux

Name:           python-usbsdmux
Version:        24.11.1
Release:        %autorelease
Summary:        USB-SD-Mux control software and library
License:        LGPL-2.1-or-later
URL:            https://github.com/linux-automation/usbsdmux/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        99-usbsdmux.rules

BuildArch:      noarch

BuildRequires:  help2man
Buildrequires:  python3-pytest
Buildrequires:  python3-pytest-mock
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

%{?python_enable_dependency_generator}

%global _description %{expand:
usbsdmux is used to control a special piece of hardware called the USB-SD-Mux.
It can be used via the command line or as a Python library
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       systemd-udev

Provides:       %{srcname} = %{version}-%{release}

Recommends:     python3-paho-mqtt

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!.*/usr/bin/env python@d}' usbsdmux/*.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-usbsdmux.rules
mkdir -p %{buildroot}%{_mandir}/man1
for BBIN in usbsdmux usbsdmux-configure ; do
    help2man --no-discard-stderr %{buildroot}%{_bindir}/$BBIN > %{buildroot}%{_mandir}/man1/$BBIN.1
done

%pyproject_save_files -l usbsdmux

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst contrib
%{_bindir}/usbsdmux*
%{_mandir}/man1/usbsdmux*1*
%{_udevrulesdir}/99-usbsdmux.rules

%changelog
%autochangelog
