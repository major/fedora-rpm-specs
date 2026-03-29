%bcond check 1

Name:           vgrep
Version:        2.8.0
Release:        %autorelease
ExclusiveArch:  %{golang_arches_future}
Summary:        User-friendly pager for grep
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://github.com/vrothberg/vgrep
Source0:        %{url}/archive/v%{version}/vgrep-%{version}.tar.gz
Source1:        vgrep-%{version}-vendor.tar.bz2

BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  askalono-cli
BuildRequires:  go-md2man


%description
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.


%prep
%autosetup -a 1


%build
# command
%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X main.version=%{version} "
%gobuild -o bin/vgrep .

# manpage
go-md2man -in docs/vgrep.1.md -out docs/vgrep.1


%install
# licenses
%go_vendor_license_install

# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/vgrep

# manpage
install -D -p -m 0644 -t %{buildroot}%{_mandir}/man1 docs/vgrep.1


%check
# license validation
%go_vendor_license_check

# upstream tests
%if %{with check}
%gocheck2
%endif


%files -f %{go_vendor_license_filelist}
%doc README.md
%{_bindir}/vgrep
%{_mandir}/man1/vgrep.1*


%changelog
%autochangelog
