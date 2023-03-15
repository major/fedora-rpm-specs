# TODO: Add tests

%global pypi_name cloudscraper

Name:           python-%{pypi_name}
Version:        1.2.62
Release:        %autorelease
Summary:        Python module to bypass Cloudflare's anti-bot page

License:        MIT 
URL:            https://github.com/venomous/cloudscraper
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm
Under Attack Mode", or IUAM), implemented with Requests. Cloudflare changes
their techniques periodically, so I will update this repo frequently.

This can be useful if you wish to scrape or crawl a website protected with
Cloudflare. Cloudflare's anti-bot page currently just checks if the client
supports Javascript, though they may add additional techniques in the future.

Due to Cloudflare continually changing and hardening their protection page,
cloudscraper requires a JavaScript Engine/interpreter to solve Javascript
challenges. This allows the script to easily impersonate a regular web browser
without explicitly deobfuscating and parsing Cloudflare's Javascript.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import -e cloudscraper.captcha.anticaptcha -e cloudscraper.captcha.capmonster -e cloudscraper.captcha.deathbycaptcha -e cloudscraper.interpreters.js2py -e cloudscraper.interpreters.v8


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
