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
    MIT AND
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

# Fix perms and drop shebangs for scripts that users are meant to copy over to
# use
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'
sed -i -e '1{\@^#!.*@d}' doc/rc/refresh

# exclude scripts for updating holiday data
rm -rf ./doc/rc/refresh
rm -rf ./scripts/addons

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
install -p -m 0755 -d $RPM_BUILD_ROOT/%{bash_completions_dir}/
install -D -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/bash/%{name}.sh $RPM_BUILD_ROOT%{bash_completions_dir}/%{name}

install -p -m 0755 -d $RPM_BUILD_ROOT/%{fish_completions_dir}/
install -D -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/fish/%{name}.fish $RPM_BUILD_ROOT%{fish_completions_dir}/%{name}.fish

# move bits to expected locations: keep this similar to task2
install -p -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/rc/* -t $RPM_BUILD_ROOT/%{_datadir}/%{name}/

# clean up
rm -rfv $RPM_BUILD_ROOT/%{_pkgdocdir}/rc
rm -fv $RPM_BUILD_ROOT/%{_pkgdocdir}/INSTALL
rm -fv $RPM_BUILD_ROOT/%{_pkgdocdir}/LICENSE
rm -frv $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/{bash,fish}

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*
%{_mandir}/man5/%{name}-color.5*
%{_mandir}/man5/%{name}-sync.5*
%dir %{_datadir}/zsh/
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_%{name}
%dir %{bash_completions_dir}
%{bash_completions_dir}/%{name}
%dir %{fish_completions_dir}
%{fish_completions_dir}/%{name}.fish
%{_datadir}/%{name}
%{_pkgdocdir}

%changelog
%autochangelog
