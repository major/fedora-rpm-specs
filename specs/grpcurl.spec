# Generated by go2rpm 1.17.1
%bcond check 1

# https://github.com/fullstorydev/grpcurl
%global goipath         github.com/fullstorydev/grpcurl
Version:                1.9.3

%gometa -L -f


Name:           grpcurl
Release:        %autorelease
Summary:        Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers

# Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        %{gosource}
# Generated by go-vendor-tools
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# https://github.com/fullstorydev/grpcurl/pull/522
Patch:          0001-test-Update-TLS-error-checks-for-Go-1.25-compatibili.patch

BuildRequires:  go-vendor-tools

%description
Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers.

%prep
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}

%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif

%files -f %{go_vendor_license_filelist}
%license vendor/modules.txt
%doc README.md
%{_bindir}/grpcurl


%changelog
%autochangelog
