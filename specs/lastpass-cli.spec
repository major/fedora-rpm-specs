Name:           lastpass-cli
Version:        1.6.1
Release:        %autorelease
Summary:        Command line interface to LastPass.com

License:        GPL-2.0-or-later WITH cryptsetup-OpenSSL-exception AND OpenSSL
URL:            https://github.com/LastPass/lastpass-cli
Source:         %url/archive/v%{version}/lastpass-cli-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1457758
Patch:          lastpass-cli-1.3.1-remove_reallocarray.patch

BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
Requires:       pinentry
Requires:       xclip

%description
A command line interface to LastPass.com.

%prep
%autosetup -p1

%build
%cmake
%cmake_build --target lpass doc-man doc-html

%install
export DESTDIR=%{buildroot}
%cmake_build --target install-doc
%cmake_install

# Install shell completions
install -Dpm0644 contrib/lpass_bash_completion -t \
    %{buildroot}%{bash_completions_dir}/lpass-completion.bash
install -Dpm0644 contrib/completions-lpass.fish -t \
    %{buildroot}%{fish_completions_dir}/lpass.fish
install -Dpm0644 contrib/lpass_zsh_completion -t \
    %{buildroot}%{zsh_completions_dir}/_lpass

%files
%license COPYING LICENSE.OpenSSL
%doc CHANGELOG.md CONTRIBUTING README.md
%doc contrib/examples %{__cmake_builddir}/lpass.1.html
%{_bindir}/lpass
%{_mandir}/man1/lpass.1*
%dir %{bash_completions_dir}
%{bash_completions_dir}/lpass-completion.bash
%dir %{fish_completions_dir}
%{fish_completions_dir}/lpass.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_lpass

%changelog
%autochangelog
