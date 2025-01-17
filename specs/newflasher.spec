Name:           newflasher
Version:        57
Release:        %autorelease
Summary:        Flash tool for new Sony flash tool protocol (Xperia XZ Premium and further)

License:        MIT
URL:            https://github.com/munjeni/newflasher
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  zlib-ng-compat-devel

%description
%{summary}.


%prep
%autosetup
sed -i "s/CFLAGS=/CFLAGS?=/" makefile


%build
%make_build


%install
install -Dpm 0755 newflasher %{buildroot}/%{_bindir}/newflasher
install -Dpm 0644 newflasher.1 %{buildroot}/%{_mandir}/man1/newflasher.1


%files
%doc readme.md
%{_bindir}/newflasher
%{_mandir}/man1/newflasher.1.*


%changelog
%autochangelog
