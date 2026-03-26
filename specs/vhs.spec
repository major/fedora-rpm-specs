%bcond check 1

%global gomodulesmode GO111MODULE=on

Name:           vhs
Version:        0.11.0
Release:        %autorelease
ExclusiveArch:  %{golang_arches_future}
Summary:        Your CLI home video recorder
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0 AND OFL-1.1
URL:            https://github.com/charmbracelet/vhs
Source0:        %{url}/archive/v%{version}/vhs-%{version}.tar.gz
Source1:        vhs-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  askalono-cli

Requires:       ttyd
Requires:       /usr/bin/ffmpeg


%description
Write terminal GIFs as code for integration testing and demoing your CLI tools.


%prep
%autosetup -p 1 -a 1


%build
export GO_LDFLAGS="-X main.Version=v%{version}"
%gobuild -o bin/vhs .


%install
# licenses
%go_vendor_license_install -c %{S:2}

# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/vhs

# man page
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/vhs man > %{buildroot}%{_mandir}/man1/vhs.1

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/vhs completion bash > %{buildroot}%{bash_completions_dir}/vhs
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/vhs completion zsh > %{buildroot}%{zsh_completions_dir}/_vhs
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/vhs completion fish > %{buildroot}%{fish_completions_dir}/vhs.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/vhs --version)" == "vhs version v%{version}" ]] || exit 1

# license validation
%go_vendor_license_check -c %{S:2}

# upstream tests
%if %{with check}
%gocheck2
%endif


%files -f %{go_vendor_license_filelist}
%{_bindir}/vhs
%{_mandir}/man1/vhs.1*
%{bash_completions_dir}/vhs
%{zsh_completions_dir}/_vhs
%{fish_completions_dir}/vhs.fish


%changelog
%autochangelog
