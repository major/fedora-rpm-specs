Name:           b43-fwcutter
Version:        021
Release:        %autorelease
Summary:        Firmware extraction tool for Broadcom wireless driver
License:        BSD-2-Clause
URL:            https://bues.ch/b43/fwcutter/
Source0:        https://bues.ch/b43/fwcutter/%{name}-%{version}.tar.xz
Source1:        https://bues.ch/b43/fwcutter/%{name}-%{version}.tar.xz.asc
# Refreshed from keyservers (same keys, newer signatures):
#   sq --home=none network keyserver search 0392335A78083894A4301C43236E8A58C6DB4512 69100FFB90E87A320DF8643CBEC39009E8321A61 757FAB7CED1814AE15B4836E5FB027474203454C --output 757FAB7CED1814AE15B4836E5FB027474203454C.gpg --overwrite
Source2:        757FAB7CED1814AE15B4836E5FB027474203454C.gpg
Source100:      README.too
BuildRequires:  gcc
BuildRequires:  openpgpverify
BuildRequires:  make

%description
This package contains the 'b43-fwcutter' tool which is used to
extract firmware for the Broadcom network devices.

See the README.too file shipped in the package's documentation for
instructions on using this tool.

%prep
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p2

cp %{SOURCE100} .

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 b43-fwcutter $RPM_BUILD_ROOT%{_bindir}/b43-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/b43-fwcutter
%{_mandir}/man1/*
%license COPYING
%doc README README.too

%changelog
%autochangelog
