Name:           bindfs
Version:        1.17.4
Release:        %autorelease
Summary:        Fuse filesystem to mirror a directory
License:        GPLv2+
URL:            http://bindfs.org/
Source0:        http://bindfs.org/downloads//bindfs-%{version}.tar.gz
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  make
# for test suite
BuildRequires:  ruby
BuildRequires:  valgrind
%if 0%{?fedora}
# Needed to mount bindfs via fstab
Recommends:     fuse
%else
Requires:     fuse
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
# Fedora's koji does not provide /dev/fuse, therefore skip the tests there
# Always cat log files on failure to be able to debug issues
#disabled tests on ppc64le until upstream fixes https://github.com/mpartel/bindfs/issues/55
%ifnarch ppc64le
if [ -e /dev/fuse ]; then
    make check || (cat tests/test-suite.log tests/internals/test-suite.log; false)
else
   # internal tests use valgrind and should work
    make -C tests/internals/ check || (cat tests/internals/test-suite.log; false)
fi
%endif

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
