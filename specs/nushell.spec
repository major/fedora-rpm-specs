Name:           nushell
Version:        0.99.1
Release:        %autorelease
Summary:        A new type of shell

SourceLicense:  MIT
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR GPL-2.0-only
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause AND MIT
# CC-PDDC
# CC0-1.0
# ISC
# MIT
# MIT AND Apache-2.0
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    MIT
    AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND (0BSD OR MIT OR Apache-2.0)
    AND Apache-2.0
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR GPL-2.0-only)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND BSD-3-Clause
    AND CC-PDDC
    AND CC0-1.0
    AND ISC
    AND (MIT OR Zlib OR Apache-2.0)
    AND (MIT-0 OR Apache-2.0)
    AND MPL-2.0
    AND Unicode-3.0
    AND (Unlicense OR MIT)
    AND Zlib
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://www.nushell.sh/
Source:         https://github.com/nushell/nushell/archive/%{version}/%{name}-%{version}.tar.gz
# drop benchmarks
# bump brotli to 7 and allow 8
# allow chrono-tz 0.8..=0.10
# allow dirs 5 to 6: https://github.com/nushell/nushell/commit/007b223acc1f0dd57ebbefc101ce1a6e46f707d0
# allow fancy-regex 0.13 to 0.16:
#   https://github.com/nushell/nushell/commit/0e3ca7b355bd62f1cfc372b414defd528da04718,
#   https://github.com/nushell/nushell/commit/1e2fa68db0f7e877fe9c4cd95ab16f1c0df793e8
# allow git2 0.19 to 0.20
# allow indicatif 0.17 to 0.18: https://github.com/nushell/nushell/pull/16248
# allow lscolors 0.17 to 0.21
# allow procfs 0.17 and which 7: https://github.com/nushell/nushell/pull/14489
# and procfs 0.18 (so >=0.16,<0.19): https://github.com/nushell/nushell/pull/17195
# and which 8: https://github.com/nushell/nushell/pull/16045
# bump quick-xml from 0.32.0 to >=0.33,<0.38
# bump reedline from 0.36 to 0.37
# bump roxmltree to 0.21: https://github.com/nushell/nushell/pull/18269
#  see also https://github.com/nushell/nushell/pull/17228, and
#  https://github.com/nushell/nushell/pull/14513 for 0.20, and note
#  that an accompanying source-code patch is required
# bump rstest to 0.26: https://github.com/nushell/nushell/pull/16359
# drop rusqlite's bundled feature
# downgrade shadow-rs from 0.35 to 0.8
# bump titlecase from 2.0 to 3.0
# bump uu_* dependencies to 0.7 and allow 0.8
# disable formats plugin; eml-parser not packaged
# disable polars plugin; polars not packaged
# disable query plugin; gsjon not packaged
# bump dialoguer from 0.11 to 0.12:
#   https://github.com/nushell/nushell/commit/839e7bb52ed21abc53497b7d91b16024ada46222
# bump lsp-server from 0.7 to 0.8:
#   https://github.com/nushell/nushell/commit/96cb2126ab9b8ac7ce1291046f854328bb77de7b
Patch:          nushell-fix-metadata.diff
Patch:          nu-command-fix-for-quick-xml-0_33.diff
Patch:          nu-command-0.99.1-roxmltree-0.21.diff
Patch:          nu-command-0.99.1-port-to-uutils-0.7.0.diff

# OOM when linking. We don't ship binaries on ix86 anyway, exclude it
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
BuildRequires:  rust2rpm-helper

Provides:       nu = 0.99.1-18
Obsoletes:      nu < 0.99.1-18

%description

The goal of Nushell is to take the Unix philosophy of shells, where pipes
connect simple commands together, and bring it to the modern style of
development. Thus, rather than being either a shell, or a programming language,
Nushell connects both by bringing a rich programming language and a
full-featured shell together into one package.

Nu takes cues from a lot of familiar territory: traditional shells like bash,
object based shells like PowerShell, gradually typed languages like TypeScript,
functional programming, systems programming, and more. But rather than trying to
be a jack of all trades, Nu focuses its energy on doing a few things well:

- Being a flexible cross-platform shell with a modern feel
- Solving problems as a modern programming language that works with the
  structure of your data
- Giving clear error messages and clean IDE support

%prep
%autosetup -p1
%cargo_prep

# borrowed from ruff

# Patch out foreign (e.g. Windows-only) dependencies. Follow symbolic links so
# that we also patch the bundled crates we just finished setting up.
find -L . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

%generate_buildrequires
%cargo_generate_buildrequires -t


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
install -Dpm 0755 target/rpm/nu -t %{buildroot}%{_bindir}


%check
# Tests fail with “too many open files” on builders where the number of cores
# is very high (e.g. 192, 224). Setting _smp_ncpus_max to 64 does not prevent
# this. Instead, more strictly constrain the number of parallel tests in
# particular. The exact number is a fairly arbitrary choice.
export RUST_TEST_THREADS=16

# * these tests depend on unshipped fixtures
%{cargo_test -- -- %{shrink:
    --skip plugin_persistence::
    --skip repl::test_custom_commands::deprecated_boolean_flag
    --skip repl::test_custom_commands::infinite_mutual_recursion_does_not_panic
    --skip repl::test_custom_commands::infinite_recursion_does_not_panic
    --skip repl::test_custom_commands::override_table_eval_file
    --skip repl::test_env::default_nu_lib_dirs_type
    --skip repl::test_env::default_nu_plugin_dirs_type
    --skip repl::test_parser::assign_backtick_quoted_external_fails
    --skip repl::test_parser::assign_backtick_quoted_external_with_caret
    --skip repl::test_parser::assign_bare_external_fails
    --skip repl::test_parser::assign_bare_external_with_caret
    --skip repl::test_parser::not_panic_with_recursive_call
    --skip repl::test_spread::spread_external_args
    --skip repl::test_spread::spread_non_list_args
    --skip const_::
    --skip eval::
    --skip hooks::
    --skip modules::
    --skip overlays::
    --skip parsing::
    --skip path::
    --skip plugin_persistence::
    --skip plugins::
    --skip scope::
    --skip shell::
}}


%files
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/nu

%changelog
%autochangelog
