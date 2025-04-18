# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/hickford/git-credential-azure
%global goipath         github.com/hickford/git-credential-azure
Version:                0.3.1

%gometa -f

%global goname git-credential-azure

%global common_description %{expand:
A Git credential helper for Azure Repos.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Git credential helper for Azure Repos

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/git-credential-azure %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp git-credential-azure.1 -t %{buildroot}%{_mandir}/man1

%if %{with check}
%check
%gocheck
%endif

%files
%{_mandir}/man1/git-credential-azure.1*
%license LICENSE.txt
%doc README.md
%{_bindir}/git-credential-azure

%changelog
%autochangelog
