%bcond check 1

%global gomodulesmode GO111MODULE=on

Name:           gum
Version:        0.17.0
Release:        %autorelease
ExclusiveArch:  %{golang_arches_future}
Summary:        Tool for glamorous shell scripts
License:        BSD-3-Clause AND MIT AND OFL-1.1
URL:            https://github.com/charmbracelet/gum
Source0:        %{url}/archive/v%{version}/gum-%{version}.tar.gz
Source1:        gum-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  askalono-cli


%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and Lip Gloss
in your scripts and aliases without writing any Go code!


%prep
%setup -q -a 1


%build
export GO_LDFLAGS="-X main.Version=v%{version}"
%gobuild -o bin/gum .


%install
# licenses
%go_vendor_license_install -c %{S:2}

# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/gum

# man page
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/gum man > %{buildroot}%{_mandir}/man1/gum.1

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/gum completion bash > %{buildroot}%{bash_completions_dir}/gum
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/gum completion zsh > %{buildroot}%{zsh_completions_dir}/_gum
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/gum completion fish > %{buildroot}%{fish_completions_dir}/gum.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/gum --version)" == "gum version v%{version}" ]] || exit 1

# license validation
%go_vendor_license_check -c %{S:2}

# upstream tests
%if %{with check}
%gocheck2
%endif


%files -f %{go_vendor_license_filelist}
%{_bindir}/gum
%{_mandir}/man1/gum.1*
%{bash_completions_dir}/gum
%{zsh_completions_dir}/_gum
%{fish_completions_dir}/gum.fish


%changelog
%autochangelog
