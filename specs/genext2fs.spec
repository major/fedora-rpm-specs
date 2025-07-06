%global commit 3b99f4a43f612b9ee74bbf24ca9890606295313f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20201011

Name:           genext2fs
Version:        1.4.2^%{commitdate}.g%{shortcommit}

Release:        %autorelease
Summary:        ext2 filesystem generator

License:        GPL-2.0-only
URL:            https://github.com/bestouff/genext2fs/
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

# clarifications for the licensing
# https://github.com/bestouff/genext2fs/pull/39
# incorrect FSF address
# https://github.com/bestouff/genext2fs/pull/38


BuildRequires:  autoconf automake
BuildRequires:  gcc
BuildRequires:  make


%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%prep
%autosetup -n %{name}-%{commit} -p1
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
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
%autochangelog
