Name:           urlscan
Version:        0.9.10
Release:        %autorelease
Summary:        Extract and browse the URLs contained in an email (urlview replacement)

License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        muttrc
Patch0:         %{name}-remove-doc.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.


%prep
%autosetup -p1
cp -p %{SOURCE1} .

# remove shebang
sed -i '/\/usr\/bin\/env.*python/ d' urlscan/__main__.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files urlscan


%files -f %{pyproject_files}
%doc muttrc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
