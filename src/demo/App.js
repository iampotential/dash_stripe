/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { StripeDash } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <StripeDash
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
