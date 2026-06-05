%bcond check    1

Name:           bear
Version:        4.1.4
Release:        %autorelease
Summary:        Tool that generates a compilation database for clang tooling

# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
                GPL-3.0-or-later
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR MIT)
                AND MIT
                AND (Unlicense OR MIT)
                }
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/rizsotto/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Manually created patch for downstream workspace metadata changes
# * Replace unpackaged serde_saphyr with serde_yaml
# * Relax mockall dependency to >0.11.4,<0.15.0
Patch:          bear-fix-metadata.diff

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
# intercept-preload explicitly requires lld to link libexec.so
BuildRequires:  lld


%description
Build ear produces compilation database in JSON format. This database describes
how single compilation unit should be processed and can be used by Clang
tooling.

%prep
%autosetup -n Bear-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
export INTERCEPT_LIBDIR=%{_lib}
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

target/rpm/generate-completions target/rpm/completions
cat > target/rpm/bear <<ENTRY_SCRIPT
#!/usr/bin/sh
exec %{_libexecdir}/bear/bin/bear-driver "\$@"
ENTRY_SCRIPT

%install
install -Dpm 0755 target/rpm/bear               -t %{buildroot}%{_bindir}
install -Dpm 0755 target/rpm/bear-driver        -t %{buildroot}%{_libexecdir}/bear/bin
install -Dpm 0755 target/rpm/bear-wrapper       -t %{buildroot}%{_libexecdir}/bear/bin
install -Dpm 0755 target/rpm/libexec.so         -t %{buildroot}%{_libexecdir}/bear/%{_lib}
install -Dpm 0644 target/rpm/completions/bear.bash %{buildroot}%{bash_completions_dir}/bear
install -Dpm 0644 target/rpm/completions/bear.fish %{buildroot}%{fish_completions_dir}/bear.fish
install -Dpm 0644 target/rpm/completions/_bear     %{buildroot}%{zsh_completions_dir}/_bear
install -Dpm 0644 man/bear.1                    -t %{buildroot}%{_mandir}/man1

%if %{with check}
%check
export INTERCEPT_LIBDIR=%{_lib} BEAR_TEST_VERBOSE=1
# Several cases fail if ccache wrappers are in the PATH.
# This is not possible in koji, but quite annoying for local builds.
cc_path=$(command -v gcc)
if [ "$cc_path" != "${cc_path%/ccache*}" ]; then
    cc_path=$(dirname "$cc_path")
    export PATH="${PATH%"$cc_path:"*}${PATH##*"$cc_path:"}"
fi
unset cc_path

%cargo_test
%endif


%files
%license COPYING
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bear
%dir %{_libexecdir}/bear
%dir %{_libexecdir}/bear/bin
%dir %{_libexecdir}/bear/%{_lib}
%{_libexecdir}/bear/bin/bear-driver
%{_libexecdir}/bear/bin/bear-wrapper
%{_libexecdir}/bear/%{_lib}/libexec.so
%{bash_completions_dir}/bear
%{fish_completions_dir}/bear.fish
%{zsh_completions_dir}/_bear
%{_mandir}/man1/bear.1*

%changelog
%autochangelog
