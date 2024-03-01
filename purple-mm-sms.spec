Name:           purple-mm-sms
Version:        0.1.7
Release:        %autorelease
Summary:        A libpurple plugin for sending and receiving SMS via ModemManager

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/purple-mm-sms
Source0:        https://source.puri.sm/Librem5/purple-mm-sms/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# Until the next release which contains this in the source
Source1:        COPYING

BuildRequires:  gcc
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(mm-glib)

# By default, the library file is installed with 0644, which breaks debuginfo.
# https://source.puri.sm/Librem5/purple-mm-sms/-/merge_requests/24
Patch0: install-library-with-correct-permissions.patch

%description
A libpurple plugin for sending and receiving SMS via ModemManager

%prep
%autosetup -p1 -n %{name}-v%{version}

# Temporary until the next release which contains this license
cp %{SOURCE1} .

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_libdir}/purple-2/mm-sms.so
%{_datadir}/pixmaps/*
%doc README.md
%license COPYING

%changelog
%autochangelog
