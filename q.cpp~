#include<bits/stdc++.h>
#define mod 1000000007
#define ll long long
using namespace std;
ll ct[26], fct[100001], tct[26], ifct[100001];
ll bpow(ll a, ll n){
    ll r = 1;
    while(n){
        if(n&1)
            r = (r * a) % mod;
        a = (a * a) % mod;
        n >>= 1;
    }
    return r;
}
int main(){
    cin.sync_with_stdio(false);
    cin.tie(0);
    ll mi4 = bpow(4, mod - 2);
    for(int i = 1;i <= 1000000000; ++i)
	mi4 = ct[0];	
    int t;
    string s;
    cin >> t;

    fct[0] = ifct[0] = 1;
    for(int i = 1;i <= 1e5; ++i) fct[i] = (i * fct[i - 1]) % mod;
    for(int i = 1;i <= 1e5; ++i) ifct[i] = bpow(fct[i], mod - 2);

    while(t--){
        cin >> s;
        memset(ct, 0, sizeof ct);
        int n = s.length();
        for(int i = 0;i < n; ++i)
            ct[(s[i] - 'a')]++;
        ll tot = fct[n], good = 1, un = 0;
        for(int i = 0;i < 26; ++i)
            tot = (tot * bpow(fct[ct[i]], mod - 2)) % mod;
        un = tot;
        tot *= tot;
        tot %= mod;
        ll ans = 0;
        for(int i = 0;i < 26; ++i){
            if(!ct[i])
                continue;
            for(int j = i + 1;j < 26; ++j){
                if(!ct[j])
                    continue;
                good = (good + ct[i] * ct[j]) % mod;
                good = (good + ((((((ct[i] * ct[j] % mod) * (ct[i] - 1) % mod) * (ct[j] - 1)) % mod) * mi4) % mod)) % mod;
                for(int k = j + 1;k < 26; ++k){
                    if(!ct[k])
                        continue;
                    good = (good + (((ct[i] * ct[j] % mod) * ct[k] % mod) * 2) % mod) % mod;
                    good = (good + (((ct[i] * ct[j] % mod) * ct[k] % mod) * (ct[i] - 1))% mod) % mod;
                    good = (good + (((ct[i] * ct[j] % mod) * ct[k] % mod) * (ct[j] - 1))% mod) % mod;
                    good = (good + (((ct[i] * ct[j] % mod) * ct[k] % mod) * (ct[k] - 1))% mod) % mod;
                    for(int l = k + 1;l < 26; ++l){
                        if(!ct[l])
                            continue;
                        ll prev = good;
                        good = (good + (((((ct[i] * ct[j] % mod) * ct[k] % mod) * ct[l]) % mod) * 3) % mod) % mod;
                    }
                }
            }
        }
        good *= un;
        good %= mod;
        tot = (tot - good + mod) % mod;

        cout << tot << "\n";
    }

}
