
Name:           zig-srpm-macros
Version:        1
Release:        1%{?dist}
Summary:        SRPM macros required for Zig packages

License:        MIT

Source0:        macros.zig-srpm
Source100:      LICENSE

BuildArch:      noarch

Requires:       rpm

%description
%{summary}

%prep
%autosetup -c -T
cp -a %{sources} .

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -pm 644 macros.* %{buildroot}%{rpmmacrodir}/

%files
%license LICENSE
%{rpmmacrodir}/macros.zig-srpm

%changelog
* Tue Oct 24 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 1-1
- Initial spec
