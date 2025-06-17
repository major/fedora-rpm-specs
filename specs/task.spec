%global forgeurl https://github.com/GothenburgBitFactory/taskwarrior

Name:           task
Version:        3.4.1
Release:        %autorelease
Summary:        Taskwarrior - a command-line TODO list manager

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# ISC AND (Apache-2.0 OR ISC)
# ISC AND (Apache-2.0 OR ISC) AND OpenSSL
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib

License:        %{shrink:
    MIT
    (Apache-2.0 OR MIT) AND BSD-3-Clause AND
    (0BSD OR MIT OR Apache-2.0) AND
    Apache-2.0 AND
    Apache-2.0 AND ISC AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    ISC AND
    ISC AND (Apache-2.0 OR ISC) AND
    ISC AND (Apache-2.0 OR ISC) AND OpenSSL AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (MIT OR Zlib OR Apache-2.0) AND
    MPL-2.0 AND
    Unicode-3.0 AND
    (Unlicense OR MIT) AND
    Zlib
}
URL:            https://taskwarrior.org
# use manually released tar because it includes the sub-module
Source0:        https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v%{version}/%{name}-%{version}.tar.gz
# generated with script below
Source1:        %{name}-%{version}-vendored.tar.xz
# To create a tarball with all crates vendored (like https://src.fedoraproject.org/rpms/loupe/blob/rawhide/f/loupe.spec)
Source2:        create-vendored-tarball.sh

# ix86: leaf removal
# does not build on s390x and ppc64
ExcludeArch:    %{ix86} s390x %{power64}

BuildRequires:  cmake
BuildRequires:  corrosion
BuildRequires:  gcc-c++

BuildRequires:  libuuid-devel

BuildRequires:  cargo-rpm-macros >= 24

%description
Taskwarrior is a command-line TODO list manager. It is flexible, fast,
efficient, unobtrusive, does its job then gets out of your way.

Taskwarrior scales to fit your workflow. Use it as a simple app that captures
tasks, shows you the list, and removes tasks from that list. Leverage its
capabilities though, and it becomes a sophisticated data query tool that can
help you stay organized, and get through your work.

%prep
%autosetup -n %{name}-%{version} -p1 -a1

echo "Running cargo prep"
%{cargo_prep -v vendor}

echo "Checking generated cargo.toml"
cat .cargo/config.toml

echo "Checking directory contents"
ls -lash
ls -lash vendor/


%build
# critical, doesn't work without this
export CARGO_HOME=%{_builddir}/%{name}-%{version}/.cargo
%cmake
%cmake_build -j1

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest

%install
export CARGO_HOME=%{_builddir}/%{name}-%{version}/.cargo
%cmake_install

# Move shell completion stuff to the right place
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm0644 scripts/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/fish/completions/
install -Dpm0644 scripts/fish/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish

# Fix perms and drop shebangs
# that's only docs and it's written in README about permissings
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'

rm -vrf %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%license LICENSE.dependencies
%doc doc/ref/%{name}-ref.pdf
%doc scripts/vim/ scripts/hooks/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*
%{_mandir}/man5/%{name}-color.5*
%{_mandir}/man5/%{name}-sync.5*
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/completions/
%{_datadir}/fish/completions/%{name}.fish

%changelog
%autochangelog
