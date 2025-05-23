Name:           python-evdev
Version:        1.9.1
Release:        %autorelease
Summary:        Python bindings for the Linux input handling subsystem

License:        BSD-3-Clause
URL:            https://python-evdev.readthedocs.io
Source0:        https://github.com/gvalkov/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  kernel-headers


%global _description \
This package provides python bindings to the generic input event interface in \
Linux. The evdev interface serves the purpose of passing events generated in \
the kernel directly to userspace through character devices that are typically \
located in /dev/input/. \
 \
This package also comes with bindings to uinput, the userspace input subsystem. \
Uinput allows userspace programs to create and handle input devices that can \
inject events directly into the input subsystem. \
 \
In other words, python-evdev allows you to read and write input events on Linux. \
An event can be a key or button press, a mouse movement or a tap on a \
touchscreen.


%description %{_description}


%package -n python3-evdev
Summary:        %{summary}
%{?python_provide:%python_provide python3-evdev}
%description -n python3-evdev %{_description}


#------------------------------------------------------------------------------
%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

#------------------------------------------------------------------------------
%build
%pyproject_wheel

#------------------------------------------------------------------------------
%install
%pyproject_install
%pyproject_save_files evdev

%check
%pyproject_check_import -t


#------------------------------------------------------------------------------
%files -n python3-evdev -f %{pyproject_files}
%license LICENSE
%doc README.md

#------------------------------------------------------------------------------
%changelog
%autochangelog
