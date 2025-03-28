# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/patrickmn/go-cache
%global goipath         github.com/patrickmn/go-cache
Version:                2.1.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-patrickmn-go-cache-devel < 2.1.0-6
}

%global common_description %{expand:
Go-cache is an in-memory key:value store/cache similar to memcached that is
suitable for applications running on a single machine. Its major advantage is
that, being essentially a thread-safe map[string]interface{} with expiration
times, it doesn't need to serialize or transmit its contents over the network.

Any object can be stored, for a given duration or forever, and the cache can be
safely used by multiple goroutines.

Although Go-cache isn't meant to be used as a persistent datastore, the entire
cache can be saved to and loaded from a file (using c.Items() to retrieve the
items map to serialize, and NewFrom() to create a cache from a deserialized one)
to recover from downtime quickly. (See the docs for NewFrom() for caveats.)}

%global golicenses      LICENSE
%global godocs          CONTRIBUTORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        In-memory key:value store/cache library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
