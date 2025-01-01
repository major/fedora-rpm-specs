Name:           ugrep
Version:        7.1.2
Release:        %autorelease
Summary:        A more powerful, ultra fast, user-friendly, compatible grep
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  brotli-devel

# Upstream does not allow building RE-flex as a shared library for ugrep to
# dynamically link against.
#
# https://github.com/Genivia/ugrep/issues/215
#
# To determine the bundled version, review the recent changes to the
# include/reflex directory.  Try to find each change in the separate RE-flex
# source.  Once you find a change that is in both, that will indicate which
# version of RE-flex is bundled.  This isn't an exact science, because changes
# happen in the bundled library first before being added to the RE-flex source.
#
# https://github.com/Genivia/ugrep/commits/master/include/reflex
# https://github.com/Genivia/RE-flex/tree/master/include/reflex
#
Provides:       bundled(libreflex) = 5.1.0


%description
Ugrep is an ultra fast, user-friendly, compatible grep.  Ugrep combines the
best features of other grep, adds new features, and searches fast.  Includes a
TUI and adds Google-like search, fuzzy search, hexdumps, searches nested
archives (zip, 7z, tar, pax, cpio), compressed files (gz, Z, bz2, lzma, xz,
lz4, zstd, brotli), pdfs, docs, and more.


%prep
%autosetup
autoreconf -fiv


%build
%ifarch %{arm}
# https://github.com/Genivia/ugrep/issues/128
%configure --disable-neon
%else
%configure
%endif
%make_build


%install
%make_install


%check
%make_build test


%files
%license LICENSE.txt
%{_bindir}/ug
%{_bindir}/ug+
%{_bindir}/ugrep
%{_bindir}/ugrep+
%{_bindir}/ugrep-indexer
%{_mandir}/man1/ug.1*
%{_mandir}/man1/ugrep.1*
%{_mandir}/man1/ugrep-indexer.1*
%{_datadir}/ugrep
%{bash_completions_dir}/ug
%{bash_completions_dir}/ug+
%{bash_completions_dir}/ugrep
%{bash_completions_dir}/ugrep+
%{bash_completions_dir}/ugrep-indexer
%{fish_completions_dir}/ug.fish
%{fish_completions_dir}/ug+.fish
%{fish_completions_dir}/ugrep.fish
%{fish_completions_dir}/ugrep+.fish
%{fish_completions_dir}/ugrep-indexer.fish
%{zsh_completions_dir}/_ug
%{zsh_completions_dir}/_ug+
%{zsh_completions_dir}/_ugrep
%{zsh_completions_dir}/_ugrep+
%{zsh_completions_dir}/_ugrep-indexer


%changelog
%autochangelog
