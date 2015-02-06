%define		_class		Pager
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	2.4.9
Release:	2
Summary:	Generic data paging class

License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Pager/
Source0:	http://download.pear.php.net/package/Pager-%{version}.tgz
Provides:	pear(Pager/Wrapper.php)
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Obsoletes:	php-pear-Pager_Sliding
BuildArch:	noarch
BuildRequires:	php-pear

%description
If you have data that needs paging (ie 1-10 on page one, 11-20 on page
two) this class can help. Pass it an array of data and it will sort it
into pages, picking up the current page id from the url. It can also
give you back/next and page number links taking the current url and
adding the correct page id to it.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml



