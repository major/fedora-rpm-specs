%global         srcname     msal-extensions
%global         forgeurl    https://github.com/AzureAD/microsoft-authentication-extensions-for-python/
Version:        1.0.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microsoft Authentication extensions for MSAL Python
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The Microsoft Authentication Extensions for Python offers secure mechanisms for
client applications to perform cross-platform token cache serialization and
persistence. It gives additional support to the Microsoft Authentication Library
for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the
SerializableTokenCache to perform cache serialization. You can read more about
this in the MSAL Python documentation. Developers are required to implement
their own cache persistance across multiple platforms and Microsoft
Authentication Extensions makes this simpler.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Remove DOS line endings
sed "s|\r||g" README.md >README.md.new && \
touch -r README.md README.md.new && \
mv README.md.new README.md


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files msal_extensions


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
