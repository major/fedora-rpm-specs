Name:           opustags
Version:        1.10.1
Release:        %autorelease
Summary:        Ogg Opus tags editor
License:        BSD-3-Clause
URL:            https://github.com/fmang/opustags

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch:          0001-Fix-out-of-bounds-access.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libogg-devel >= 1.3.3

BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Symbol)
BuildRequires:  ffmpeg-free

%description
Opustags allows you to view and edit Ogg Opus comments. It supports the
following features:
* interactive editing using your preferred text editor,
* batch editing with command-line flags,
* tags exporting and importing through text files.

%prep
%autosetup -p1 -C

%build
%cmake
%cmake_build

%install
%cmake_install
rm -r %{buildroot}/%{_docdir}/opustags

%check
%cmake_build --target check

%files
%{_bindir}/opustags
%license LICENSE
%{_mandir}/man1/opustags.1.gz

%changelog
%autochangelog
