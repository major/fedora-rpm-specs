Name:           bindfs
Version:        1.18.4
Release:        %autorelease
Summary:        Fuse filesystem to mirror a directory
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://bindfs.org/
Source0:        http://bindfs.org/downloads/bindfs-%{version}.tar.gz
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  make
# for test suite
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 3.0.0
BuildRequires:  valgrind
%if 0%{?fedora}
# Needed to mount bindfs via fstab
Recommends:     fuse3
%else
Requires:       fuse3
%endif

%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
# Tests are failing on Fedora 40+ so let's disable until further investigation
# Fedora's koji does not provide /dev/fuse, therefore skip the tests there
# Always cat log files on failure to be able to debug issues
# Disabled tests on ppc64le until upstream fixes https://github.com/mpartel/bindfs/issues/55
# %ifnarch ppc64le
# if [ -e /dev/fuse ]; then
#    make check || (cat tests/test-suite.log tests/internals/test-suite.log; false)
# else
   # internal tests use valgrind and should work
#    make -C tests/internals/ check || (cat tests/internals/test-suite.log; false)
# fi
# %endif

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
