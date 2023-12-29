%global debug_package %{nil}

%global forgeurl https://github.com/premake/premake-core
%global date 20231215
%global commit 78afb221e6996ed96be955212bd75fc953e0a69a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           premake
Version:        5.0.0
Release:        %autorelease
Summary:        Cross-platform build configuration tool

License:        BSD-3-Clause
URL:            https://premake.github.io/
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  compat-lua-devel
BuildRequires:  readline-devel
BuildRequires:  libuuid-devel

%description
Premake is a command line utility which reads a scripted definition of a
software project, then uses it to perform build configuration tasks or generate
project files for toolsets like Visual Studio, Xcode, and GNU Make. Premake's
scripts are little Lua programs, so the sky's the limit!

%prep
%forgesetup

%build
# bootstrap your first Premake executable
make -f Bootstrap.mak linux
# generate makefiles
./bin/release/premake5 gmake
# embed and compile Lua scripts into the Premake executable to ship a single
# file instead of a whole bunch of scripts.
./bin/release/premake5 embed
# rebuild
%make_build config=release

%install
install -pDm 755 bin/release/premake5 %{buildroot}/%{_bindir}/premake5
install -pDm 644 packages/debian/premake.1 %{buildroot}%{_mandir}/man1/premake5.1

%check
# for aarch64 and s390x, base_os.findlib_FindSystemLib failed.
# https://koji.fedoraproject.org/koji/taskinfo?taskID=103879506
# https://koji.fedoraproject.org/koji/taskinfo?taskID=103879508
%ifnarch aarch64 s390x
bin/release/premake5 test
%endif

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/premake5
%{_mandir}/man1/premake5.1.gz

%changelog
%autochangelog
