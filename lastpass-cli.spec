Name:           lastpass-cli
Version:        1.3.4
Release:        %autorelease
Summary:        Command line interface to LastPass.com

License:        GPL-2.0-only
URL:            https://github.com/LastPass/lastpass-cli
Source0:        %url/archive/v%{version}/lastpass-cli-%{version}.tar.gz

# RHBZ#1457758
Patch0:         lastpass-cli-1.3.1-remove_reallocarray.patch
# https://github.com/lastpass/lastpass-cli/issues/532
Patch1:         0001-Mark-global-variable-as-extern.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  asciidoc
BuildRequires: make
Requires:       pinentry
Requires:       xclip

%description
A command line interface to LastPass.com.

%prep
%autosetup -p1

%build
%cmake .
%make_build

%install
%make_install install-doc

# Install shell completions
install -Dpm0644 contrib/lpass_bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/lpass-completion.bash
install -Dpm0644 contrib/completions-lpass.fish \
    %{buildroot}%{_datadir}/fish/vendor_functions.d/lpass.fish
install -Dpm0644 contrib/lpass_zsh_completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_lpass

%files
%license COPYING
%license LICENSE.OpenSSL
%doc README.md
%doc CONTRIBUTING
%doc contrib/examples
%{_bindir}/lpass
%{_mandir}/man1/lpass.1.*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/lpass-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/lpass.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_lpass

%changelog
%autochangelog
