Name:           genext2fs
Version:        1.6.2
Release:        %autorelease
Summary:        ext2 filesystem generator

License:        GPL-2.0-only
URL:            https://github.com/bestouff/genext2fs/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# clarifications for the licensing
# https://github.com/bestouff/genext2fs/pull/39
# incorrect FSF address
# https://github.com/bestouff/genext2fs/pull/38


BuildRequires:  autoconf automake
BuildRequires:  gcc
BuildRequires:  make
# test
BuildRequires:  attr
BuildRequires:  e2fsprogs
BuildRequires:  python3


%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%prep
%autosetup -p1
autoreconf -fi


%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
%autochangelog
